import { serve } from "https://deno.land/std@0.168.0/http/server.ts"
import { createClient } from "https://esm.sh/@supabase/supabase-js@2"

const SUPABASE_URL = "https://ncfeudprexwdvwcnlhtx.supabase.co"
const SERVICE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im5jZmV1ZHByZXh3ZHZ3Y25saHR4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3NjEwNTYzMywiZXhwIjoyMDkxNjgxNjMzfQ.eL_DbszSHx4J1hfDf0KnudOoR2qDLL5tAQC6iYjAHS0"

serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "*" } })
  }
  try {
    const body = await req.json()
    const eventType = body.event_type
    console.log("Event:", eventType, JSON.stringify(body).substring(0, 500))

    let payerEmail = ""
    let txnId = ""

    if (eventType === "CHECKOUT.ORDER.COMPLETED") {
      payerEmail = body.resource?.payer?.email_address || body.resource?.payment_source?.paypal?.email_address || ""
      txnId = body.resource?.id || ""
    } else if (eventType === "PAYMENT.SALE.COMPLETED") {
      payerEmail = body.resource?.payer?.payer_info?.email || ""
      txnId = body.resource?.id || ""
    }

    console.log("Payer email:", payerEmail, "Txn:", txnId)

    if (payerEmail) {
      const supabase = createClient(SUPABASE_URL, SERVICE_KEY)
      const { error } = await supabase
        .from("users")
        .update({ is_premium: true, paypal_txn_id: txnId })
        .eq("email", payerEmail)
      if (error) console.error("DB error:", error)
      else console.log("Unlocked premium for", payerEmail)
    }

    return new Response("OK", { status: 200 })
  } catch (e) {
    console.error("Error:", e)
    return new Response("Error", { status: 500 })
  }
})
