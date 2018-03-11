import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class HelloWindow(Gtk.Window):
    def __init__(self):

        # Call super init
        Gtk.Window.__init__(self, title='Hello, World!')

        # Create a button
        self.button = Gtk.Button(label='Click Me!')

        """
        Add a handler for `clicked` event
        General syntax:
        widget.connect('event', callback, data)
        """
        self.button.connect('clicked', self.click_handler)

        new_handler_id = self.button.connect('released', self.release_handler)

        # Add button to window as a child
        self.add(self.button)

    # Called when button is clicked
    def click_handler(self, widget):
        print('Button clicked!')

    # Called when button is released
    def release_handler(self, widget):
        print('Button released!')


win = HelloWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()

Gtk.main()
