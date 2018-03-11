import gi
# Specify version of Gtk
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# Create a window
win = Gtk.Window()

# Closes but doesn't exit from shell?
win.connect('delete-event', Gtk.main_quit)

# Make window and all the widgets contained inside it visible
win.show_all()

# Start the main loop
Gtk.main()
