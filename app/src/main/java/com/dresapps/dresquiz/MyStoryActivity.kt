package com.dresapps.dresquiz

import android.app.AlertDialog
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.dresapps.dresquiz.databinding.ActivityMyStoryBinding

class MyStoryActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMyStoryBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMyStoryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnViewStory.setOnClickListener {
            AlertDialog.Builder(this)
                .setTitle("\uD83D\uDCDA My Story")
                .setMessage("A Message to You\n\nYou picked up this phone today.\n\nMaybe to pass time. Maybe someone sent you the link. Either way you are here now, and that matters.\n\nEvery Caribbean student who has ever felt like the system wasn\'t built for them this was made for you. Not to replace school. Just to give you an edge at the thing that can quietly change the direction of your life: your CXC exams.\n\nThe world is loud. Social media is louder. But somewhere in the middle of all that noise, your grades are still the one thing no one can take from you.\n\nYou don\'t have to be perfect. You just have to keep going.\n\nPlay this game like it matters. Because one day when you\'re holding your results slip you\'ll remember that you prepared. You\'ll remember that you showed up.\n\nThat\'s the version of you worth becoming.\n\nPlay hard. Study harder.\n\nAndré N. John")
                .setPositiveButton("Close", null)
                .show()
        }

        binding.btnBackStory.setOnClickListener { finish() }
    }
}