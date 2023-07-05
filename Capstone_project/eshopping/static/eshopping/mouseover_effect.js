// mouse over shadow effect
document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('mouseover', event => {
        const element = event.target;
        if (element.className === "item_box"){
            //console.log("item box");
            document.getElementById(element.id).style.opacity = 0.5;
        };
        if (element.className === "image_block"){
            //console.log("image block");
            document.getElementById(element.parentElement.id).style.opacity = 0.5;
        }
        if (element.nodeName === "IMG"){
            //console.log("img tag");
            if (element.parentElement.className === "image_block"){
                document.getElementById(element.parentElement.parentElement.id).style.opacity = 0.5;
            }
        }
        
    });
});
document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('mouseout', event => {
        const element = event.target;
        if (element.className === "item_box"){
            //console.log("item box");
            document.getElementById(element.id).style.opacity = 1.0;
        };
    });
});