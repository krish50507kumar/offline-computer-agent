import pyautogui as gui
import time
class Tools:
    def __init__(self):
        self.tool_used = []
        self.tools = {
            "click":self.click,
            "double_click":self.double_click,
            "move_mouse":self.move_mouse,
            "type_text":self.type_text,
            "press_key":self.press_key,
            "hot_key":self.hot_key,
            "scroll":self.scroll,
            "drag":self.drag,
            "wait":self.wait,
            "alert":self.alert,
            "get_screen_info":self.get_screen_info,
        }
    def click(self,x,y):
        gui.click(x,y)
    def double_click(self,x,y):
        gui.doubleClick(x,y)
    def move_mouse(self, x, y):
        gui.moveTo(x, y)
    def type_text(self,text):
        gui.write(text, interval=0.25)
    def press_key(self,key):
        gui.press(key)
    def hot_key(self,keys):
        gui.hotkey(*keys)
    def scroll(self,amount):
        gui.scroll(amount)
    def drag(self, start_x, start_y, end_x, end_y, duration, button="left"):
        gui.moveTo(start_x, start_y)
        gui.dragTo(end_x, end_y, duration=duration, button=button)

    def wait(self, seconds):
        time.sleep(seconds)
    def alert(self,text):
        gui.alert(text)
    def get_screen_info(self):
        sx,sy = gui.size()
        return f"screen: width={sx}, height={sy}"

    def action(self, act):
        tool = act["tool"]
        params = act["params"]
        self.tool_used.append(tool)
        return self.tools[tool](**params)

