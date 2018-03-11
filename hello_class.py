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
        self.button.connect('clicked', self.button_handler)

        # Get all properties
        print(dir(self.button.props))

        # Get specific property
        print(self.button.get_property('label'))

        # Change some arbitary properties
        self.button.set_property('label', 'Mellow, World!!')

        # Change alignment
        print('({},{})'.format(
            self.button.get_property('xalign'),
            self.button.get_property('yalign')))
        
        self.button.set_property('xalign', 0.7)
        self.button.set_property('yalign', 0.9)

        # Change margin
        print(self.button.get_property('margin'))

        self.button.set_property('margin', 10)

        # Add button to window as a child
        self.add(self.button)

    # Called when button is clicked
    def button_handler(self, widget):
        print('Hello, World!')


win = HelloWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()

Gtk.main()
