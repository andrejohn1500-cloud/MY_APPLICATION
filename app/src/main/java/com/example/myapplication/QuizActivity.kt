package com.example.myapplication

import android.content.Intent
import android.media.AudioAttributes
import android.media.AudioManager
import android.media.ToneGenerator
import android.media.SoundPool
import android.os.Bundle
import android.os.CountDownTimer
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityQuizBinding

class QuizActivity : AppCompatActivity() {

    private lateinit var binding: ActivityQuizBinding
    private lateinit var questions: List<Question>
    private var currentIndex = 0
    private var score = 0
    private var answered = false
    private var timer: CountDownTimer? = null
    private lateinit var soundPool: SoundPool
    private var sndCorrect = 0
    private var sndWrong   = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityQuizBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val category = intent.getStringExtra("category") ?: QuestionBank.categories[0]
        questions = QuestionBank.getQuestions(category).shuffled()
        binding.tvCategory.text = category

        val attrs = AudioAttributes.Builder()
            .setUsage(AudioAttributes.USAGE_GAME)
            .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
            .build()
        soundPool = SoundPool.Builder().setMaxStreams(2).setAudioAttributes(attrs).build()
        // Add res/raw/correct.mp3 and res/raw/wrong.mp3 then uncomment:
        // sndCorrect = soundPool.load(this, R.raw.correct, 1)
        // sndWrong   = soundPool.load(this, R.raw.wrong,   1)

        val options = listOf(binding.btnOption0, binding.btnOption1,
                             binding.btnOption2, binding.btnOption3)
        options.forEachIndexed { i, btn -> btn.setOnClickListener { handleAnswer(i, options) } }
        loadQuestion(options)
    }

    private fun loadQuestion(options: List<Button>) {
        if (currentIndex >= questions.size) { goToResult(); return }
        answered = false
        val q = questions[currentIndex]
        binding.tvProgress.text = "Question ${currentIndex + 1} of ${questions.size}"
        binding.tvQuestion.text  = q.text
        binding.tvScore.text     = "Score: $score"
        options.forEachIndexed { i, btn ->
            btn.text = q.options[i]
            btn.setBackgroundResource(R.drawable.bg_option_default)
            btn.setTextColor(getColor(R.color.white))
            btn.isEnabled = true
        }
        startTimer(options)
    }

    private fun startTimer(options: List<Button>) {
        timer?.cancel()
        binding.progressTimer.max = 30
        timer = object : CountDownTimer(30_000L, 1_000L) {
            override fun onTick(ms: Long) {
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
            options[selected].setBackgroundResource(R.drawable.bg_option_correct)
            ToneGenerator(AudioManager.STREAM_MUSIC, 90).startTone(ToneGenerator.TONE_PROP_BEEP, 250)
        } else {
            options[selected].setBackgroundResource(R.drawable.bg_option_wrong)
            ToneGenerator(AudioManager.STREAM_MUSIC, 90).startTone(ToneGenerator.TONE_PROP_NACK, 400)
            showCorrect(options)
        }
        disableAll(options)
        nextDelayed(options)
    }

    private fun showCorrect(options: List<Button>) {
        options[questions[currentIndex].correctIndex]
            .setBackgroundResource(R.drawable.bg_option_correct)
    }

    private fun disableAll(options: List<Button>) = options.forEach { it.isEnabled = false }

    private fun nextDelayed(options: List<Button>) {
        binding.root.postDelayed({
            currentIndex++
            loadQuestion(options)
        }, 1300)
    }

    private fun goToResult() {
        startActivity(
            Intent(this, ResultActivity::class.java).apply {
                putExtra("score",    score)
                putExtra("total",    questions.size)
                putExtra("category", binding.tvCategory.text.toString())
            }
        )
        finish()
    }

    override fun onDestroy() {
        super.onDestroy()
        timer?.cancel()
        soundPool.release()
    }
}
