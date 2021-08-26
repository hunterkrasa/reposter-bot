from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import random
import config

preferences_set = False
last_number = 10
browser = webdriver.Firefox(executable_path = config.pathway)
browser.get('https://www.instagram.com/')

# login_link = browser.find_element_by_xpath("//a[text()='Log in']")
# login_link.click()
# sleep(2)
print("Instagram successfully opened!")
sleep(3)
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(config.instagram_username)
password_input.send_keys(config.instagram_pass)

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

print("Login Successful")

sleep(8)

notifs = browser.find_element_by_xpath("//button[text() = 'Not Now']")
notifs.click()

sleep(5)

notifs = browser.find_element_by_xpath("//button[text() = 'Not Now']")
notifs.click()

sleep(3)
	

while True:
	post_type = ".mp4"
	searchbar = browser.find_element_by_xpath("//input[@type = 'text']")
	

	sleep(2)


	number = random.randint(0, (len(config.account_list) - 1))
	account = config.account_list[number]

	if last_number == number:
		new_number = random.randint(0, (len(config.account_list) - 1))
		account = config.account_list[new_number]

	last_number = number

	print("Posting from " + account)

	sleep(3)

	searchbar.send_keys(account)

	sleep(5)


	user_click = browser.find_element_by_partial_link_text(account)
	user_click.click()

	sleep(2)

	first_picture = browser.find_element_by_class_name('eLAPa')
	print("First picture opened")
	first_picture.click()

	sleep(2)

	try:
		video_play = browser.find_element_by_class_name("videoSpritePlayButton")
	except: 
		post_type = ".jpeg"
	finally:

		browser_url = browser.current_url
		trimmed_url = browser_url[28:(len(browser_url) - 1)]
		print(browser_url)
		print(trimmed_url)
		print(post_type)


		post_url = browser.current_url

		sleep(3)

		new_browser = webdriver.Firefox(executable_path = config.pathway)
		new_browser.get("https://repostapp.com")
		print("Opened repost app successfully")

		sleep(2)

		repost_search = new_browser.find_element_by_css_selector("input")
		repost_search.click()
		repost_search.send_keys(post_url)

		print("Repost Loading...")

		sleep(75)

		d_vid = new_browser.find_element_by_xpath("//*[contains(text(), 'Download')]")
		d_vid.click()

		sleep(1)

		caption_copy_one = new_browser.find_element_by_xpath("//button[@id = 'option-menu']")
		caption_copy_one.click()
		sleep(1)
		caption_copy_two = new_browser.find_element_by_xpath("//*[contains(text(), 'Copy Caption')]")
		caption_copy_two.click()


		if preferences_set == False:
			print("Paused for user input...")
			verify = input("Type y to continue")

			if verify == "y":
				preferences_set = True
				print("Verification Successful")



		sleep(3)

		new_browser.close()


		close = browser.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Close"]')
		close.click()

		sleep(2)

		video_selection = browser.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="New Post"]')
		video_selection.click()

		sleep(3)

		video_selection = browser.find_element_by_xpath("//input[@accept = 'image/jpeg,image/png,video/mp4,video/quicktime']")
		video = config.video_base + "repost-" + account + "-" + trimmed_url + post_type
		print(video)
		video_selection.send_keys(video)

		print("Passed video selection")

		sleep(3)

		# post_size = browser.find_element_by_xpath("//button[text() = 'Next']")
		post_size = browser.find_element_by_class_name("sqdOP.L3NKy._4pI4F.y3zKF.cB_4K")
		post_size.click()
		print("Clicked one")

		sleep(1)
		post_filters = browser.find_element_by_class_name("sqdOP.L3NKy._4pI4F.y3zKF.cB_4K")
		post_filters.click()
		sleep(1)

		caption = browser.find_element_by_class_name("lFzco")


		caption_choice = random.randint(0, 6)
		caption_final = config.caption_list[caption_choice] + pyperclip.paste()
		caption.send_keys(caption_final)

		print("Caption Pasted")

		share_post = browser.find_element_by_xpath("//button[text() = 'Share']")
		share_post.click()

		print("Post shared!")

		sleep(10)

		close = browser.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="svg"][@aria-label="Close"]')
		close.click()

		print("Time for sleep!")

		sleep(90000)





# browser.close()
