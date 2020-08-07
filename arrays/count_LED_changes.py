# Program For counting the total changes in the LED after displaying the number
# of digits given as input string.
# Very easy approach would be to precompute the led's lighted up as and when any
# number between 0-9, is displayed.
# so, let's assume the display is seven segement display.
# Now, 0 : displayed by 6 led's, and similar all others.
# precomputed array , LED : : [ 6, 2, 5, 5, 4, 5, 6, 3, 7, 5 ]
# Now, simply we can initialize our sum as first digit value and then iterate
# through the input string, and count the changes in the led as
# LED[i] - LED[i - 1], as this will no. of led's that changed when we displayed
# char at i transitioning from i - 1.
# So, let's say, n = "082", 0 would lighten up 6 led's, and now when displayed 8
# would switch on one extra light, so 6 + 1 = 7 so far.
# Now, 2 would switch off 2 extra led's, and so, 7 + 2 = 9
# Hence, total 9 times LED's toggled.
