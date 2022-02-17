# TEMP_MAIL

Forget about spam, advertising mailings, hacking and attacking robots. Keep your real mailbox clean and secure. Temp Mail provides temporary, secure, anonymous, free, disposable email address.

We will be using only 2 python libraries That are re and request. If you don’t have them already installed, use the commands below to install them:

```pip
pip3 install request
pip3 install re
```

Generate Gmail
The very first step is to subscribe to the Temp-Gmail API via [Rapid API](https://rapidapi.com/mrsonj/api/temp-gmail/) (It’s totally free).

Note that the input “ID” is just an integer that corresponds to a specific Gmail address in the API dataset (contains 1000 Gmails). If you change the value of “ID”, the function will generate a different Gmail address.

Check Inbox
All right, now that we have created a temporary Gmail address, we can check its inbox. The check_inbox(gmail: str, password: str) function scans for the new incoming mails.
If there is none, it returns a message that the inbox is empty.

Read inbox Message
In order to read the content of the mail, we should have the Gmail address and the message_id. If we send a request to the API providing these two values, the API returns the body message in the HTML format with all those HTML tags attached to it.

Hence, we may use the re library to remove the HTML tags and print the cleaned body message.

Restore Gmail
As mentioned at the beginning of this tutorial, temporary emails expire after a certain time limit (Usually after 10 minutes).
Meaning that the password will be reset! Therefore, If you have created a Gmail address and want to reaccess it after a period of time, you need to restore it.
The restore_gmail(gmail: str) function takes your already generated Gmail address and sets a new password for it so it can be reused.
