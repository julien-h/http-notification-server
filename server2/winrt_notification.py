import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom

#create notifier
nManager = notifications.ToastNotificationManager
notifier = nManager.create_toast_notifier()

#define your notification as string
tString = """
<toast>
    <visual>
        <binding template='ToastGeneric'>
            <text>Sample toast</text>
            <text>Sample content</text>
        </binding>
    </visual>
</toast>
"""

#convert notification to an XmlDocument
xDoc = dom.XmlDocument()
xDoc.load_xml(tString)

#display notification
notifier.show(notifications.ToastNotification(xDoc))