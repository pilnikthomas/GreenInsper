import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd

email_user = 'greeninsper@gmail.com' #email do GreenInsper
email_password = '' #senha
email_send='' #variavel aberta pra enviar o email

subject = 'GreenInsper: Reserve sua garrafa' #assunto do email

msg = MIMEMultipart() #chamando a biblioteca
msg['From'] = email_user #email "de"
msg['To'] = email_send #email "para"
msg['Subject'] = subject #assunto do email

#corpo de texto
body = 'Olá!\n\nNo nosso formulário, você selecionou a opção de pré-venda! As garrafas chegaram mais cedo do que esperávamos e por isso decidimos por não realizar a pré-venda.\n\nNo entanto, iremos te reservar a sua, e você pode vir buscar no horário das vendas! Para garantir sua garrafa, responda esse email com seu nome completo, modelo escolhido (modelo que já vendemos ou modelo novo, ou você pode optar pela garrafinha da Bateria!) e quantidade!\n\nLembrando que as vendas acontecerão nos dias 16, 17 e 18 de Abril, entre 11:30 e 13:30 e entre 17:30 e 21:30!\n\nTe esperamos lá!\n\nGreenInsper'
msg.attach(MIMEText(body,'plain')) #juntando corpo

part = MIMEBase('application','octet-stream')
part.add_header('Content-Disposition',"attachment; filename= ")

text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587) #server do gmail
server.starttls()
server.login(email_user,email_password) #fazendo login

form = pd.read_csv('greeninsper.csv',sep=',') #abrindo o formulário

email_df= pd.DataFrame(form.loc[:, ["Q13"]]) #definindo um dataframe apenas com a coluna de emails
email_df=email_df.dropna() #retirando as linhas que não possuem emails

lista=[] #lista vazia
for i in email_df.Q13: #percorrendo os emails
	lista.append(i)  #adicionando os emails a uma lista

lista.pop(0) #retirando o enunciado
lista.pop(0) #retirando o "import"

for email_python in lista_nova: #para cada email na lista
	email_send=email_python #definindo o destinatário como esse email
	server.sendmail(email_user,email_send,text) #e enviando

server.quit() #saindo do servidor