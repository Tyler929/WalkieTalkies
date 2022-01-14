## Walikie Talkies Jekyll

## Website Description
A website to display art from students at Del Norte with a rotating gallery so art student's will be able to showcase their work online and get recognition.


| Kamya's Weekly Work | Kaavya's Weekly Work| Katie's Weekly Work | Tyler's Weekly Work |
| --------------- | --------------- | --------------- |--------------- |
| [Kamya's Commits](https://github.com/Tyler929/WalkieTalkies/tree/commitskamya ) | |
|  |[Kaavya's's Commits](https://github.com/Tyler929/WalkieTalkies/commits?author=rkaavya) | |
| | |  [Katie's Commits](https://github.com/Tyler929/WalkieTalkies/commits?author=katiehickman) |
| |  | | [Tyler's Commits]( https://github.com/Tyler929/WalkieTalkies/commits?author=Tyler929)| https://github.com/Tyler929/WalkieTalkies/commits?author=Tyler929|

![Image](https://www.architectureartdesigns.com/wp-content/uploads/2013/12/20-Absolutely-Stunning-Art-Pieces-for-Your-Home-3.jpg)

 ## Our favorite code segement 
 
 ```markdown
Syntax highlighted code block
  // Hack: add java script function to toggle image from original to gray and back (toggle)
        //  document.getElementById("img<n>").src
        //  document.getElementID("img_gray<n>").innerHTML
        //  help: https://www.geeksforgeeks.org/how-to-change-the-src-attribute-of-an-img-element-in-javascript-jquery/
        <!-- used var instead to toggle grayscale values and dynamically change rgb values -->
        <!-- var is defining a variable and 2 is assigned to colorscale and 1 is assigned to grayscale-->
        var imageType = 2;
        function toggle() {
            if (imageType == 2) {
                $('#colorscale').hide()
                $('#grayscale').show()
                imageType = 1; <!-- allows for toggling back and forth -->
            } else {
                $('#grayscale').hide()
                $('#colorscale').show()
                imageType = 2; <!-- allows for toggling back and forth -->
            }
        }

```


