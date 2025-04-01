import dearpygui.dearpygui as dpg

def add_text_to_console():
	# dpg.set_value("console", dpg.get_value("console") + "some_text\n")
	dpg.add_text("some_text", parent="console_window")
	dpg.set_y_scroll("console_window", dpg.get_y_scroll_max("console_window"))

def add_long_text():
	dpg.add_text("veeeerrrrryyyyyyyy looooonnnnggggggggggggg tteeeeeeeeeexxxxxxxttttttttttttt!!!!!!!",
	parent="console_window")
	dpg.set_y_scroll("console_window", dpg.get_y_scroll_max("console_window"))

def add_error_msg_to_console():
	dpg.add_text("[error] something went wrong", parent="console_window", color=(196, 43, 43))
	dpg.set_y_scroll("console_window", dpg.get_y_scroll_max("console_window"))

def add_goog_msg_to_console():
	dpg.add_text("this is very goog msg!", parent="console_window", color=(69, 214, 69))
	dpg.set_y_scroll("console_window", dpg.get_y_scroll_max("console_window"))

dpg.create_context()


with dpg.window(label="Console"):
	with dpg.group(horizontal=True):
		dpg.add_button(label="Add text to console", callback=add_text_to_console)
		dpg.add_button(label="Add long text", callback=add_long_text)
		dpg.add_button(label="Add error msg", callback=add_error_msg_to_console)
		dpg.add_button(label="Add goog msg", callback=add_goog_msg_to_console)

	with dpg.child_window(horizontal_scrollbar=True, width=500, height=300, tag="console_window"):	
		pass
	with dpg.group(horizontal=True):
		dpg.add_input_text()
		dpg.add_button(label="send", width=75)
		#dpg.bind_font(default_font)
		dpg.create_viewport(title='Custom Title', width=800, height=600)

dpg.setup_dearpygui()

dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context() 