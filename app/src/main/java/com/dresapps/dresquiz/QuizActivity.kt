package com.dresapps.dresquiz

import android.content.Intent
import android.media.AudioAttributes
import android.media.AudioManager
import android.media.ToneGenerator
import android.media.SoundPool
import android.os.Bundle
import android.os.CountDownTimer
import android.view.View
import android.view.animation.AnimationUtils
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import androidx.cardview.widget.CardView
import com.dresapps.dresquiz.databinding.ActivityQuizBinding
import com.google.android.material.button.MaterialButton
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.LoadAdError
import com.google.android.gms.ads.FullScreenContentCallback
import com.google.android.gms.ads.interstitial.InterstitialAd
import com.google.android.gms.ads.interstitial.InterstitialAdLoadCallback

class QuizActivity : AppCompatActivity() {

    private lateinit var binding: ActivityQuizBinding
    private lateinit var questions: List<Question>
    private var currentIndex = 0
    private var score = 0
    private var level = 1
    private var answered = false
    private var timer: CountDownTimer? = null
    private lateinit var soundPool: SoundPool
    private var sndCorrect = 0
    private var sndWrong  = 0
    private var cheatsUsed  = 0
    private var timerPaused = false
    private var interstitialAd: InterstitialAd? = null
    private var timeLeftMs  = 30_000L

    private val correctRemarks = listOf(
        "Hypothesis confirmed!",
        "Even Einstein nods!",
        "My calculations approve!",
        "Neurons firing perfectly!",
        "Peer reviewed: CORRECT!",
        "The data backs you up!",
        "Science is proud today.",
        "Lab results: Genius.",
        "Outstanding specimen!",
        "That answer is certified!"
    )

    private val wrongRemarks = listOf(
        "Back to the lab...",
        "My coffee was wrong too.",
        "Gravity gets it wrong too.",
        "Needs peer review...",
        "I have seen worse. Barely.",
        "Recalibrating expectations.",
        "The universe forgives you.",
        "Plot twist nobody wanted.",
        "Even Darwin struggled.",
        "Science is still your friend."
    )

    private val timerRemarks = listOf(
        "Time: just a suggestion.",
        "The clock was the villain.",
        "Einstein bent time too.",
        "Thinking is not a crime.",
        "Speed is overrated anyway."
    )

    
    private fun loadInterstitialAd() {
        val adRequest = AdRequest.Builder().build()
        InterstitialAd.load(this, "ca-app-pub-3890705518764486/7970502313", adRequest,
            object : InterstitialAdLoadCallback() {
                override fun onAdLoaded(ad: InterstitialAd) {
                    interstitialAd = ad
                }
                override fun onAdFailedToLoad(error: LoadAdError) {
                    interstitialAd = null
                }
            })
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val vib = getSystemService(android.content.Context.VIBRATOR_SERVICE) as android.os.Vibrator
        fun buzz() {
            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
                vib.vibrate(android.os.VibrationEffect.createOneShot(25, android.os.VibrationEffect.DEFAULT_AMPLITUDE))
            } else { vib.vibrate(25) }
        }

        binding = ActivityQuizBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val category = intent.getStringExtra("category") ?: "CXC Maths"
        level = intent.getIntExtra("level", 1)
        questions = QuestionLoader.loadQuestions(this, category, level).map { q ->
    val shuffled = q.options.shuffled()
    q.copy(options = shuffled, correctIndex = shuffled.indexOf(q.options[q.correctIndex]))
}.shuffled()
        binding.tvCategory.text = category

        val attrs = AudioAttributes.Builder()
            .setUsage(AudioAttributes.USAGE_GAME)
            .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
            .build()
        soundPool = SoundPool.Builder().setMaxStreams(2).setAudioAttributes(attrs).build()

        val options = listOf(
            binding.btnOption0, binding.btnOption1,
            binding.btnOption2, binding.btnOption3
        )

        options.forEachIndexed { i, btn ->
            btn.setOnClickListener { buzz(); handleAnswer(i, options) }
        }

        loadQuestion(options)

        binding.btnCheat.setOnClickListener {
            buzz()
            ToneGenerator(AudioManager.STREAM_MUSIC, 90).startTone(ToneGenerator.TONE_PROP_BEEP2, 150)
            if (answered) return@setOnClickListener
            if (!timerPaused) {
                timer?.cancel()
                timerPaused = true
                cheatsUsed++
                binding.btnCheat.text = "Resume"
            } else {
                timerPaused = false
                binding.btnCheat.text = "Cheat"
                startTimerFrom(timeLeftMs, options)
            }
        }
    }

    private fun loadQuestion(options: List<Button>) {
        if (currentIndex >= questions.size) { goToResult(); return }
        answered = false
        timerPaused = false
        binding.btnCheat.isEnabled = true
        binding.btnCheat.alpha = 1.0f
        binding.btnCheat.text = "Cheat"
        val q = questions[currentIndex]
        binding.tvProgress.text = "Question ${currentIndex + 1} of ${questions.size}"
        binding.tvQuestion.text  = q.text
        binding.tvScore.text     = "Score: $score"

        options.forEachIndexed { i, btn ->
            btn.text = q.options[i]
            btn.isEnabled = true
            btn.setTextColor(getColor(R.color.white))
            (btn as? MaterialButton)?.backgroundTintList =
                android.content.res.ColorStateList.valueOf(
                    android.graphics.Color.TRANSPARENT
                )
        }
        startTimer(options)
    }

    private fun startTimer(options: List<Button>) {
        timer?.cancel()
        binding.progressTimer.max = 30
        timer = object : CountDownTimer(30_000L, 1_000L) {
            override fun onTick(ms: Long) {
                timeLeftMs = ms
                val secs = (ms / 1000).toInt()
                binding.tvTimer.text = "⏱ $secs"
                binding.progressTimer.progress = secs
                binding.tvTimer.setTextColor(
                    if (secs <= 5) getColor(R.color.wrong) else getColor(R.color.gold)
                )
            }
            override fun onFinish() {
                if (!answered) {
                    binding.tvTimer.text = "⏱ 0"
                    showCorrect(options)
                    disableAll(options)
                    showScientist(timerRemarks.random())
                    nextDelayed(options)
                }
            }
        }.start()
    }

    private fun handleAnswer(selected: Int, options: List<Button>) {
        if (answered) return
        answered = true
        timer?.cancel()
        val q = questions[currentIndex]

        if (selected == q.correctIndex) {
            score++
            setButtonFill(options[selected], "#1DB954")
            ToneGenerator(AudioManager.STREAM_MUSIC, 90)
                .startTone(ToneGenerator.TONE_PROP_BEEP, 250)
            showScientist(correctRemarks.random())
        } else {
            setButtonFill(options[selected], "#E74C3C")
            setButtonFill(options[q.correctIndex], "#1DB954")
            ToneGenerator(AudioManager.STREAM_MUSIC, 90)
                .startTone(ToneGenerator.TONE_PROP_NACK, 400)
            showScientist(wrongRemarks.random())
        }

        disableAll(options)
        nextDelayed(options)
    }

    private fun showScientist(remark: String) {
        val card = findViewById<CardView>(R.id.scientistCard) ?: return
        binding.tvScientistRemark.text = remark
        card.visibility = View.VISIBLE
        card.alpha = 0f
        card.translationX = 300f
        card.animate()
            .alpha(1f)
            .translationX(0f)
            .setDuration(350)
            .withEndAction {
                card.postDelayed({
                    card.animate()
                        .alpha(0f)
                        .translationX(300f)
                        .setDuration(180)
                        .withEndAction { card.visibility = View.GONE }
                        .start()
                }, 1200)
            }
            .start()
    }

    private fun setButtonFill(btn: Button, hexColor: String) {
        (btn as? MaterialButton)?.backgroundTintList =
            android.content.res.ColorStateList.valueOf(
                android.graphics.Color.parseColor(hexColor)
            )
    }

    private fun showCorrect(options: List<Button>) {
        setButtonFill(options[questions[currentIndex].correctIndex], "#1DB954")
    }

    private fun disableAll(options: List<Button>) {
        options.forEach { it.isEnabled = false }
        binding.btnCheat.isEnabled = false
        binding.btnCheat.alpha = 0.4f
    }

    private fun nextDelayed(options: List<Button>) {
        binding.root.postDelayed({
            currentIndex++
            loadQuestion(options)
        }, 1300)
    }

    private fun goToResult() {
        if (interstitialAd != null) {
            interstitialAd!!.fullScreenContentCallback = object : FullScreenContentCallback() {
                override fun onAdDismissedFullScreenContent() {
                    interstitialAd = null
                    loadInterstitialAd()
                    startActivity(Intent(this@QuizActivity, ResultActivity::class.java).apply {
                        putExtra("score",    score)
                        putExtra("total",    questions.size)
                        putExtra("category", binding.tvCategory.text.toString())
                        putExtra("level", level)
            putExtra("cheats",     cheatsUsed)
                        putExtra("time_taken", ((30_000L - timeLeftMs) / 1000).toInt())
                    })
                    finish()
                }
            }
            interstitialAd!!.show(this)
        } else {
            startActivity(Intent(this, ResultActivity::class.java).apply {
                putExtra("score",    score)
                putExtra("total",    questions.size)
                putExtra("category", binding.tvCategory.text.toString())
                putExtra("level", level)
            putExtra("cheats",     cheatsUsed)
                        putExtra("time_taken", ((30_000L - timeLeftMs) / 1000).toInt())
            })
            finish()
        }
    }

    private fun startTimerFrom(fromMs: Long, options: List<Button>) {
        timer?.cancel()
        timer = object : CountDownTimer(fromMs, 1_000L) {
            override fun onTick(ms: Long) {
                timeLeftMs = ms
                val secs = (ms / 1000).toInt()
                binding.tvTimer.text = "⏱ ${secs}s"
                binding.progressTimer.progress = secs
                binding.tvTimer.setTextColor(
                    if (secs <= 5) getColor(R.color.wrong) else getColor(R.color.gold)
                )
            }
            override fun onFinish() {
                if (!answered) {
                    binding.tvTimer.text = "⏱ 0s"
                    showCorrect(options)
                    disableAll(options)
                    showScientist(timerRemarks.random())
                    nextDelayed(options)
                }
            }
        }.start()
    }

    override fun onDestroy() {
        super.onDestroy()
        timer?.cancel()
        soundPool.release()
    }
}
