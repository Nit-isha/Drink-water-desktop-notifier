import time
from plyer import notification

if __name__ == '__main__':
    count = 200
    while True:
        
        left = 2200 - count
        if left < 0:
            break
        msg = "You have to drink 2.2L water every day. Till now you drank " + str(count) + " mililitres.\n" + "Well Done! " + str(left) + "ml to go.."
        count += 200
        notification.notify(
            
            title = "Please drink water",
            message = msg,
            timeout = 5,
            app_name = 'Reminder',
            app_icon = 'drink-water.ico'
            
        )
        time.sleep(60*60)