###################################################
# APS106 - Winter 2022 - Lab 8 - Corner Detection #
###################################################

from lab8_image_utils import display_image, image_to_pixels
from operator import itemgetter

################################################
# PART 1 - RGB to Grayscale Conversion         #
################################################

def rgb_to_grayscale(rgb_img):
    """
    (tuple) -> tuple
    
    Function converts an image of RGB pixels to grayscale.
    Input tuple is a nested tuple of RGB pixels.
    
    The intensity of a grayscale pixel is computed from the intensities of
    RGB pixels using the following equation
    
        grayscale intensity = 0.3 * R + 0.59 * G + 0.11 * B
    
    where R, G, and B are the intensities of the R, G, and B components of the
    RGB pixel. The grayscale intensity should be *rounded* to the nearest
    integer.
    """
    
    ## TODO complete the function
    grey_scale = []
    
    #going through each nested tuple and applying function
    for pixel in rgb_img:
        grey_scale.append(round(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2]))
        
    return tuple(grey_scale)

############################
# Part 2b - Dot Product    #
############################

def dot(x,y):
    """
    (tuple, tuple) -> float
    
    Performs a 1-dimensional dot product operation on the input vectors x
    and y. 
    """
    collector = 0
    
    #iterating through the vectors and doing dot product
    for i in range(len(x)):
        collector += x[i]*y[i]
        
    return collector
######################################
# Part 2c - Extract Image Segment    #
######################################

def extract_image_segment(img, width, height, centre_coordinate, N):
    """
    (tuple, int, int, tuple, int) -> tuple
    
    Extracts a 2-dimensional NxN segment of a image centred around
    a given coordinate. The segment is returned as a tuple of pixels from the
    image.
    
    img is a tuple of grayscale pixel values
    width is the width of the image
    height is the height of the image
    centre_coordinate is a two-element tuple defining a pixel coordinate
    N is the height and width of the segment to extract from the image
    
    """
    ## TODO complete the function
    
    #This block takes in the centre coodinates, and gets a range of x and y values from those
    #coordinates. I will combine them in the next block
    x_coordinates = range(int(centre_coordinate[0]-(N-2)/2), int(centre_coordinate[0]+(N-2)/2)+2)
    y_coordinates = range(int(centre_coordinate[1]-(N-2)/2), int(centre_coordinate[1]+(N-2)/2)+2)
    
    #print(x_coordinates)
    #print(y_coordinates)
    
    '''
    #I reduced this code to the function below. Uncomment this block if you want to understand
    #what i did earlier
    cood_list = []
    for y in y_coordinates:
        for x in x_coordinates:
            cood_list.append([x,y])
            
    new_cood = []
    for coord in cood_list:
        new_cood.append(coord[1]*width + (coord[0] + 1))
    '''     
    
    #In this step, I am iterating through those x and y values generated and then converting it into 
    #coordinates that are readable in the given tuple. Think about like this, I am taking the y and multiplying
    #it by the width in order to get the number of row items before the desired coordinate, then i add the 
    #x value to get the full amount
    
    cood_list = []
    for y in y_coordinates:
        for x in x_coordinates:
            cood_list.append(y*width + (x + 1))
            
    #print(cood_list)
    
    #print(new_cood)
    
    #I am taking the converted values from cood_list and extracting the from the IMG tuple
    return_list = []
    for i in cood_list:
        return_list.append(img[i-1])

    return tuple(return_list)


######################################
# Part 2d - Kernel Filtering         #
######################################

def kernel_filter(img, width, height, kernel):
    """
    (tuple, int, int, tuple) -> tuple
    
    Apply the kernel filter defined within the two-dimensional tuple kernel to 
    image defined by the pixels in img and its width and height.
    
    img is a 1 dimensional tuple of grayscale pixels
    width is the width of the image
    height is the height of the image
    kernel is a 2 dimensional tuple defining a NxN filter kernel, n must be an odd integer
    
    The function returns the tuple of pixels from the filtered image
    """

    ## TODO complete the function
    
    #Here i am just turning the kernel into a format that is easier to use
    kernel_tuple = []
    for i in kernel:
        for k in i:
            kernel_tuple.append(k)
    
    #print(kernel_tuple)
    
    #Here I figured out the N value, which is important for the extract_image_segment Function
    N = len(kernel_tuple)**(0.5)
     
    #im creating all the x and x coordinates that i will need to test
    x_coordinates = range(int((N-1)/2), width-int((N-1)/2))
    y_coordinates = range(int((N-1)/2), height-int((N-1)/2))
    
    #im creating an array of empty zeros that i will update and eventually return
    end_array = []
    for i in range(width*height):
        end_array.append(0)
    
    
    
    
    
    #print(N)
    
    #U know the x and y coordinated that i said i needed to determine the values for?
    #i'm using it here and iterating through all of that
    for y in y_coordinates:
        for x in x_coordinates:
            
            #im taking the segment of pixels i want to test in this block
            segment = extract_image_segment(img, width, height, (x,y), N)
            #print("segment",segment)
            #print("dot,", dot(segment,kernel_tuple))
            
            #I'm doing the dot product thingy, where im multipling two matrices together here
            #then im updating the required coordinates in the end_array, that i will eventually return
            end_array[y*width + (x)] = int(dot(segment,kernel_tuple))  
    
    return tuple(end_array)
 
###############################
# PART 3 - Harris Corners     #
###############################

def harris_corner_strength(Ix,Iy):
    """
    (tuple, tuple) -> float
    
    Computes the Harris response of a pixel using
    the 3x3 windows of x and y gradients contained 
    within Ix and Iy respectively.
    
    Ix and Iy are  lists each containing 9 integer elements each.

    """

    # calculate the gradients
    Ixx = [0] * 9
    Iyy = [0] * 9
    Ixy = [0] * 9
    
    for i in range(len(Ix)):
        Ixx[i] = (Ix[i] / (4*255))**2
        Iyy[i] = (Iy[i] / (4*255))**2
        Ixy[i] = (Ix[i] / (4*255) * Iy[i] / (4*255))
    
    # sum  the gradients
    Sxx = sum(Ixx)
    Syy = sum(Iyy)
    Sxy = sum(Ixy)
    
    # calculate the determinant and trace
    det = Sxx * Syy - Sxy**2
    trace = Sxx + Syy
    
    # calculate the corner strength
    k = 0.03
    r = det - k * trace**2
    
    return r

def harris_corners(img, width, height, threshold):
    """
    (tuple, int, int, float) -> tuple
    
    Computes the corner strength of each pixel within an image
    and returns a tuple of potential corner locations. Each element in the
    returned tuple is a two-element tuple containing an x- and y-coordinate.
    The coordinates in the tuple are sorted from highest to lowest corner
    strength.
    """
    
    # perform vertical edge detection
    vertical_edge_kernel = ((-1, 0, 1),
                            (-2, 0, 2),
                            (-1, 0, 1))
    Ix = kernel_filter(img, width, height, vertical_edge_kernel)
    
    # perform horizontal edge detection
    horizontal_edge_kernel = ((-1,-2,-1),
                              ( 0, 0, 0),
                              ( 1, 2, 1))
    Iy = kernel_filter(img, width, height, horizontal_edge_kernel)
    
    # compute corner scores and identify potential corners
    border_sz = 1
    corners = []
    for i_y in range(border_sz, height-border_sz):
        for i_x in range(border_sz, width-border_sz):
            Ix_window = extract_image_segment(Ix, width, height, (i_x, i_y), 3)
            Iy_window = extract_image_segment(Iy, width, height, (i_x, i_y), 3)
            corner_strength = harris_corner_strength(Ix_window, Iy_window)
            if corner_strength > threshold:
                #print(corner_strength)
                corners.append([corner_strength,(i_x,i_y)])

    # sort
    corners.sort(key=itemgetter(0),reverse=True)
    corner_locations = []
    for i in range(len(corners)):
        corner_locations.append(corners[i][1])

    return tuple(corner_locations)


###################################
# PART 4 - Non-maxima Suppression #
###################################

def non_maxima_suppression(corners, min_distance):
    """
    (tuple, float) -> tuple
    
    Filters any corners that are within a region with a stronger corner.
    Returns a tuple of corner coordinates that are at least min_distance away from
    any other stronger corner.
    
    corners is a tuple of two-element coordinate tuples representing potential
        corners as identified by the Harris Corners Algorithm. The corners
        are sorted from strongest to weakest.
    
    min_distance is a float specifying the minimum distance between any
        two corners returned by this function
    """
    
    ## TODO complete the function
    
    #this is the float thingy that we want to return
    F =[]
    
    #we are going to iterate through all the corners
    for coord in corners:
        #print("f",F)
        #print("coord",coord)
        flag = True
        
        #in this loop, we are going to test the corner to all the F in that array
        for f_coord in F:
            
            #checking if the distance between F coordinate and corner coordinate
            distance = ((f_coord[0]-coord[0])**2+(f_coord[1]-coord[1])**2)**(0.5)
            
            #print(distance)
            #check if the distance is more than min distance, if so, we add it to a flag
            if distance < min_distance:
                flag = False
        
        #basically if there are not comparisons where the distance is larger than
        #min distance, add the coord to the F
        if flag:
            F.append(coord)  
    
    return tuple(F)
