package com.example.myapplication

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityDonationBinding

class DonationActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDonationBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDonationBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnPayPal.setOnClickListener {
            val intent = Intent(Intent.ACTION_VIEW,
                Uri.parse("https://www.paypal.com/donate/?business=andrejohn1500%40gmail.com&currency_code=USD"))
            startActivity(intent)
        }
        binding.btnBackDonate.setOnClickListener { finish() }
    }
}
