import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class HelloWindow(Gtk.Window):

    def __init__(self):

        # Call super init
        Gtk.Window.__init__(self, title='Hello, World!')

        # Create a button
        self.button = Gtk.Button(label='Click Me!')
        
        # Add a handler for `clicked` event
        # Try out having additional parameters in handler
        self.button.connect('clicked', lambda widget: self.button_handler(widget, self.button))

        # Add button to window as a child
        self.add(self.button)

    # Called when button is clicked
    def button_handler(self, widget, something):
        print(something)

win = HelloWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()

Gtk.main()
