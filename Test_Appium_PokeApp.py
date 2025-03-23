from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración de capacidades
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.app = r"C:\\Users\\danie\\OneDrive\\Desktop\\Appium\\PokeApp.apk"
options.automation_name = "UiAutomator2"



def login():
    
    # Esperar que cargue la pantalla de login
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='password']"))
    )
    time.sleep(1)  # Sleep for 3 seconds to let the page settle

    # Ingresar contraseña y enviar formulario
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='password']")))
    password_input = driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='password']")
    password_input.send_keys("CsF2ty9vjx@VHpbZq7")
    submit_button = driver.find_element(By.XPATH, "//android.widget.Button[@text='Submit']")  # Update the locator if needed
    submit_button.click()                           
    time.sleep(1)
    return

def seleccionar_opciones(driver, set_value, type_value, rarity_value, card_name=None):
  
    time.sleep(0.4)
    # 2. Esperar y seleccionar el valor para "set_name"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.view.View[@resource-id='set_name']")))
    set_dropdown = driver.find_element(By.XPATH, "//android.view.View[@resource-id='set_name']")
    set_dropdown.click()
    set_option = driver.find_element(By.XPATH, f"//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='{set_value}']")
    set_option.click()
    print(f"✔ Seleccionado: {set_value}")

    # 3. Esperar y seleccionar el valor para "type"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.view.View[@resource-id='type']")))
    type_dropdown = driver.find_element(By.XPATH, "//android.view.View[@resource-id='type']")
    type_dropdown.click()
    type_option = driver.find_element(By.XPATH, f"//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='{type_value}']")
    type_option.click()
    print(f"✔ Seleccionado: {type_value}")

    # 4. Esperar y seleccionar el valor para "rarity"
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.view.View[@resource-id='rarity']")))
    rarity_dropdown = driver.find_element(By.XPATH, "//android.view.View[@resource-id='rarity']")
    rarity_dropdown.click()
    rarity_option = driver.find_element(By.XPATH, f"//android.widget.CheckedTextView[@resource-id='android:id/text1' and @text='{rarity_value}']")
    rarity_option.click()
    print(f"✔ Seleccionado: {rarity_value}")

     # 1. Si se proporciona un valor para el nombre de la carta, ingresarlo en el campo correspondiente
    if card_name:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='name']")))
        name_input = driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='name']")
        name_input.clear()  # Limpiar el campo antes de ingresar el nuevo valor
        name_input.send_keys(card_name)  # Ingresar el nombre de la carta
        print(f"✔ Ingresado nombre de la carta: {card_name}")


def scroll_down_and_up(driver):
    # Scroll down for 1 second (this can be achieved by scrolling with a delay)
    driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollForward()')
    
    # Wait for 1 second before scrolling back to the top
    driver.save_screenshot("appium_test_screenshot1.png")
    time.sleep(1)
    
    # Scroll back to the top
    driver.find_element(By.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()).scrollToBeginning(10)')

    print("Scrolled down for 1 second and then back to the top.")


def click_add_card_button(driver):
    try:
        # Wait until the "Add Card" button is visible
        add_card_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Add Card']"))
        )

        # Click the "Add Card" button
        add_card_button.click()
        print("Clicked the 'Add Card' button successfully.")
    
    except Exception as e:
        print(f"Error while clicking the 'Add Card' button: {str(e)}")


def fill_and_add_card(driver):
    try:
        # Wait for the first EditText field to be visible (pre-mbp-074)
        pre_mbp_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='id']"))
        )
        pre_mbp_field.send_keys("pre-mbp-074")
        print("Filled pre-mbp-074.")

        # Wait for the next EditText field (name)
        name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='name']"))
        )
        name_field.send_keys("Eevee")
        print("Filled Eevee.")

        # Wait for the set_name field to be visible
        set_name_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='set_name']"))
        )
        set_name_field.send_keys("Prismatic Evolutions")
        print("Filled Prismatic Evolutions.")

        # Wait for the image_url field to be visible
        image_url_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='image_url']"))
        )
        image_url_field.send_keys("https://tcgplayer-cdn.tcgplayer.com/product/610691_in_800x800.jpg")
        print("Filled image URL.")

        # Wait for the trend_price field to be visible
        trend_price_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='trend_price']"))
        )
        trend_price_field.send_keys("29.64")
        print("Filled trend price.")


        # Wait for the regulation field to be visible
        regulation_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='regulation']"))
        )
        regulation_field.send_keys("H")
        print("Filled regulation.")

        # Now wait for the 'Add Card' button to be clickable
        add_card_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Add Card']"))
        )
        add_card_button.click()
        print("Clicked 'Add Card' button.")

    except Exception as e:
        print(f"Error: {str(e)}")

def click_owned_button(driver):
    # Find the first button by XPath and click it
    check_owned_pokemon_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Check Owned Pokémon']")))
    check_owned_pokemon_button.click()
    

def click_clear_button(driver):
    # Find the second button by XPath and click it
    clear_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@resource-id="clear-button"]')))
    clear_button.click()


def scroll_down_and_up(driver, max_swipes=1):
    # Get the screen size
    screen_size = driver.get_window_size()
    width = screen_size['width']
    height = screen_size['height']


    # Scroll up
    for _ in range(max_swipes):
        driver.swipe(width / 2, height * 0.8, width / 2, height * 0.2, 800)  # Swipe up
        time.sleep(1)  # Wait for the screen to update


    # Scroll down
    for _ in range(max_swipes):
        driver.swipe(width / 2, height * 0.2, width / 2, height * 0.8, 800)  # Swipe down
        time.sleep(1)  # Wait for the screen to update




try:
    #Paso 1: Iniciar lacionexion y abrir el APK
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    print("Driver conectado con éxito")


    #Paso 2:. Iniciar Sesion en el APK
    login()

    #Paso 3: Seleccionar opciones en los dropdowns y agregar un nombre a la carta (set, type, rarity, name)
    seleccionar_opciones(driver, "Prismatic Evolutions", "Fire", "Full Art", "")
    time.sleep(0.2)

    #Paso 4:
    scroll_down_and_up(driver)
    time.sleep(0.5)

    #Paso 5: Seleccionar opciones en los dropdowns y agregar un nombre a la carta (set, type, rarity, name)
    seleccionar_opciones(driver, "151", "Grass", "Full Art", "")
    time.sleep(0.2)

    #Paso 6:
    scroll_down_and_up(driver)
    time.sleep(0.5)


    #Paso 5:
    click_add_card_button(driver)
    time.sleep(4)
    
    #Paso 6
    fill_and_add_card(driver)
    time.sleep(4)

    #Paso7
    click_owned_button(driver)
    scroll_down_and_up(driver)
    time.sleep(1)

    #Paso8
    click_clear_button(driver)
    time.sleep(2)

    # Cerrar la sesión
    driver.quit()

except Exception as e:
    print("Error al ejecutar Appium:", e)
    if 'driver' in locals():
        driver.quit()
