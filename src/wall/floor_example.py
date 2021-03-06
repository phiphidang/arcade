import simplegui, time, random
class Constants:
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = WINDOW_WIDTH
    GLOBAL_DEFAULT_SQUARE_SIZE = 25

    GRID_WIDTH = WINDOW_WIDTH / GLOBAL_DEFAULT_SQUARE_SIZE
    GRID_HEIGHT = GRID_WIDTH

    DEFAULT_FLOOR_HEIGHT = 10
class Floor:
    FLOOR_HEIGHT = Constants.DEFAULT_FLOOR_HEIGHT
    GRID_HEIGHT = Constants.GRID_HEIGHT
    
    def __init__(self, active_blocks, height=FLOOR_HEIGHT):
        self.active_blocks = active_blocks
        self.height = height
        
    def draw_me(self, canvas):
        for i in self.active_blocks:
            self.Rect.Square((i,self.GRID_HEIGHT - self.height)).draw_me(canvas)

    class Rect:

        def rect_coords (length, height, startpos = (0, 0)) :
            x = startpos[0]
            y = startpos[1]
            return [
                (x, y),
                (x, y + height),
                (x + length, y + height),
                (x + length, y)  
            ] 

        class Square:
            
            DEFAULT_SQUARE_DRAW_ATTRIBUTES = {
                "line_width": 1,
                "line_color": 'Green',
                "fill_color": 'Orange'
            }

            SHAPE_ATTRIBUTES = DEFAULT_SQUARE_DRAW_ATTRIBUTES
            SIZE = Constants.GLOBAL_DEFAULT_SQUARE_SIZE

            def __init__(self, top_left_pt, size=SIZE, shape_attributes=SHAPE_ATTRIBUTES):
                self.top_left_point = top_left_pt
                self.shape_attributes = shape_attributes
                self.size = size

            def draw_me(self, canvas):
                size = self.size
                (x,y) = self.top_left_point
                (x,y) = x*size, y*size
                canvas.draw_polygon(Floor.Rect.rect_coords(size, size, (x,y)),
                    self.shape_attributes["line_width"],
                    self.shape_attributes["line_color"],
                    self.shape_attributes["fill_color"]
                )

floor = Floor(range(3) + range(6,9))
floor2 = Floor(range(5,6) + range(10,29))


def draw(canvas):
    floor.draw_me(canvas)
    floor2.draw_me(canvas)

    
    
    
    
    
    
class Graphics:
    
    WINDOW_WIDTH = Constants.WINDOW_WIDTH
    WINDOW_HEIGHT = Constants.WINDOW_HEIGHT
    
    def __init__(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        frame = simplegui.create_frame("Home", width, height)
        frame.set_canvas_background("Silver")
        frame.set_draw_handler(draw)
        frame.start()
Graphics()
              
