from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://127.0.0.1:5500/IHM/index.html")

def localizar_elementos():
    global name_input, email_input, telefone_input, message_input, submit_button, form
    form = driver.find_element(By.ID, "formContato")
    name_input = driver.find_element(By.ID, "name")
    email_input = driver.find_element(By.ID, "email")
    telefone_input = driver.find_element(By.ID, "telefone")
    message_input = driver.find_element(By.ID, "message")
    submit_button = driver.find_element(By.CSS_SELECTOR, "input.enviar")

def rolar_para_formulario():
    form = driver.find_element(By.ID, "formContato")
    driver.execute_script("arguments[0].scrollIntoView(true);", form)
    time.sleep(1)


localizar_elementos()
rolar_para_formulario()

# Teste 1: Email válido e telefone inválido
print("Teste 1: Email válido e telefone inválido")
name_input.send_keys("Fulano da Siva")
time.sleep(1)
email_input.send_keys("fulano.silva@example.com")
time.sleep(1)
telefone_input.send_keys("abcd")
time.sleep(1)
message_input.send_keys("Teste de mensagem.")
time.sleep(2)

submit_button.click()
time.sleep(2)

localizar_elementos()
name_input.clear()
email_input.clear()
telefone_input.clear()
message_input.clear()

# Teste 2: Telefone válido e email inválido
print("Teste 2: Telefone válido e email inválido")
rolar_para_formulario()
name_input.send_keys("Fulano da Silva")
time.sleep(1)
email_input.send_keys("email_invalido")
time.sleep(1)
telefone_input.send_keys("(92) 91234-5678")
time.sleep(1)
message_input.send_keys("Teste de mensagem.")
time.sleep(2)

submit_button.click()
time.sleep(2)

localizar_elementos()
name_input.clear()
email_input.clear()
telefone_input.clear()
message_input.clear()

# Teste 3: Todos os dados válidos
print("Teste 3: Todos os dados válidos")
rolar_para_formulario()
name_input.send_keys("Fulano da Silva")
time.sleep(1)
email_input.send_keys("fulano.silva@example.com")
time.sleep(1)
telefone_input.send_keys("(91) 91234-5678")
time.sleep(1)
message_input.send_keys("Teste de mensagem válida.")
time.sleep(2)

submit_button.click()
time.sleep(10)

print("Formulário enviado com dados válidos. Verifique se foi processado corretamente.")

driver.quit()
