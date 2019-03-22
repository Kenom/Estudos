import psutil
import smtplib


#Sistema de Monitoramento#


# print(psutil.cpu_times())

x = 0.0
processamento = 0
proc_result = 0


def seding_mail():
        # credentials
        remetente = 'kenombr@gmail.com'
        senha = 'xxxxxxxxx'

        # information destination and title/context
        destinatario = 'maia_wesley@outlook.com'
        assunto = 'Monitoramento Kenom'
        texto = ('FALHA NO HARDWARE')

        # preparing e-mail for send
        msg = '\r\n'.join([
            'From: %s' % remetente,
            'To: %s' % destinatario,
            'Subject: %s' % assunto,
            '',
            '%s' % texto
            ])

        # sending e-mail
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg)
        server.quit()

for x in range(10):
    processamento = (psutil.cpu_percent(interval=1))
    proc_result = proc_result + processamento
    print(proc_result)

resultado = proc_result / 10
