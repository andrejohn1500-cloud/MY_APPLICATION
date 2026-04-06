import re

# ── STEP 1: Add popup layout to activity_quiz.xml ──
xml_path = "./app/src/main/res/layout/activity_quiz.xml"
with open(xml_path, "r") as f:
    xml = f.read()

popup_xml = '''
    <!-- Scientist Popup -->
    <androidx.cardview.widget.CardView
        android:id="@+id/scientistCard"
        android:layout_width="220dp"
        android:layout_height="wrap_content"
        android:layout_marginTop="12dp"
        android:layout_marginEnd="12dp"
        android:layout_gravity="top|end"
        android:visibility="gone"
        app:cardCornerRadius="16dp"
        app:cardBackgroundColor="#1A1E3A"
        app:cardElevation="8dp">

        <LinearLayout
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:orientation="horizontal"
            android:padding="10dp"
            android:gravity="center_vertical">

            <TextView
                android:id="@+id/tvScientistFace"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:text="🧑‍🔬"
                android:textSize="28sp"
                android:paddingEnd="8dp"/>

            <TextView
                android:id="@+id/tvScientistRemark"
                android:layout_width="0dp"
                android:layout_height="wrap_content"
                android:layout_weight="1"
                android:textColor="#FFD700"
                android:textSize="11sp"
                android:textStyle="italic"
                android:text="Remark here"/>

        </LinearLayout>
    </androidx.cardview.widget.CardView>'''

# Insert before closing root tag
if 'scientistCard' not in xml:
    xml = xml.replace('</FrameLayout>', popup_xml + '\n</FrameLayout>')
    if 'scientistCard' not in xml:
        xml = xml.replace('</LinearLayout>', popup_xml + '\n</LinearLayout>', 1)

with open(xml_path, "w") as f:
    f.write(xml)
print("✅ Scientist popup card added to XML")

# ── STEP 2: Update QuizActivity.kt ──
kt_path = "./app/src/main/java/com/example/myapplication/QuizActivity.kt"
with open(kt_path, "r") as f:
    kt = f.read()

new_kt = '''package com.example.myapplication

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
import com.example.myapplication.databinding.ActivityQuizBinding
import com.google.android.material.button.MaterialButton

class QuizActivity : AppCompatActivity() {

    private lateinit var binding: ActivityQuizBinding
    private lateinit var questions: List<Question>
    private var currentIndex = 0
    private var score = 0
    private var answered = false
    private var timer: CountDownTimer? = null
    private lateinit var soundPool: SoundPool
    private var sndCorrect = 0
    private var sndWrong  = 0

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

        val options = listOf(
            binding.btnOption0, binding.btnOption1,
            binding.btnOption2, binding.btnOption3
        )

        options.forEachIndexed { i, btn ->
            btn.setOnClickListener { handleAnswer(i, options) }
        }

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
                        .setDuration(300)
                        .withEndAction { card.visibility = View.GONE }
                        .start()
                }, 2000)
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

    private fun disableAll(options: List<Button>) =
        options.forEach { it.isEnabled = false }

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
'''

with open(kt_path, "w") as f:
    f.write(new_kt)
print("✅ QuizActivity.kt updated with scientist popup system")
