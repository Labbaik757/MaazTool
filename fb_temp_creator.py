import requests, random, string, time, names
from playwright.sync_api import sync_playwright

# 🔧 Generate random email for TempMail
def generate_email():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(["1secmail.com", "esiix.com", "wwjmp.com"])
    return name, f"{name}@{domain}"

# 💬 Get inbox for email
def get_inbox(login, domain):
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    return requests.get(url).json()

# 📩 Get message content (activation code link)
def read_message(login, domain, msg_id):
    url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={msg_id}"
    return requests.get(url).json()

# 🔐 Main account creation logic
def create_account():
    fname = names.get_first_name()
    lname = names.get_last_name()
    login, email = generate_email()
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + "@"

    print(f"\n🌐 Creating Facebook account with {email}")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            page.goto("https://www.facebook.com/reg")
            time.sleep(2)

            page.fill('input[name=firstname]', fname)
            page.fill('input[name=lastname]', lname)
            page.fill('input[name=reg_email__]', email)
            time.sleep(2)
            page.fill('input[name=reg_email_confirmation__]', email)
            page.fill('input[name=reg_passwd__]', password)

            page.select_option('select[name=birthday_day]', str(random.randint(1, 28)))
            page.select_option('select[name=birthday_month]', str(random.randint(1, 12)))
            page.select_option('select[name=birthday_year]', str(random.randint(1985, 2002)))

            page.click('input[value="2"]')  # Male
            page.click('button[name=websubmit]')
            print("📤 Submitted form. Waiting for OTP...")

            # Wait and fetch OTP
            time.sleep(20)
            otp_code = None
            for _ in range(10):
                inbox = get_inbox(login, email.split("@")[1])
                if inbox:
                    msg_id = inbox[0]['id']
                    body = read_message(login, email.split("@")[1], msg_id)
                    otp_code = body['body'].split("FB-")[1][:5]
                    print(f"📨 OTP Received: {otp_code}")
                    break
                time.sleep(5)

            if otp_code:
                page.fill('input[name=code]', otp_code)
                page.click('button[type=submit]')
                print("✅ Account Created and Confirmed!")
                with open("created_accounts.txt", "a") as f:
                    f.write(f"{email}|{password}\n")
            else:
                print("❌ OTP not received. Account may not be confirmed.")

        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            browser.close()


def main():
    count = int(input("🔢 How many accounts to create using TempMail? "))
    for i in range(count):
        create_account()
        print(f"✅ Finished account #{i+1}\n")
        time.sleep(random.randint(10, 20))

if __name__ == "__main__":
    main()
