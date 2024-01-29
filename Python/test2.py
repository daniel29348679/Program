# %%
import smtplib
from email.mime.text import MIMEText

mime = MIMEText(
    "測試內文",  # 撰寫內文內容
    "plain",
    "utf-8",
)  # 撰寫內文內容，以及指定格式為plain，語言為中文
mime["Subject"] = "test測試"  # 撰寫郵件標題
mime["From"] = "曾品元大神"  # 撰寫你的暱稱或是信箱
mime["To"] = "林同學"  # 撰寫你要寄的人
mime["Cc"] = ""  # 副本收件人
msg = mime.as_string()  # 將msg將text轉成str
print(msg)
smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.ehlo()  # 申請身分
smtp.starttls()  # 加密文件，避免私密信息被截取
smtp.login("daniel29348679@gmail.com", "tgdx kfac mwea bvhp")
from_addr = "daniel29348679@gmail.com"
to_addr = ["cindylin911105@gmail.com"]
status = smtp.sendmail(from_addr, to_addr, msg)
print("success" if status == {} else "failed")
smtp.quit()
