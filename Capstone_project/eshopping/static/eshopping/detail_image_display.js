document.addEventListener('DOMContentLoaded', function() {
    document.addEventListener('click', event => {
        const element = event.target;
        //console.log(element);
        if (element.className === "small_image"){
            //console.log(image_no);
            //console.log(element);

            // Check if the large image block is cover image or not
            const large_image = document.getElementsByClassName("large_image");
            //console.log(large_image[0])
            if (large_image[0].id == 'image_0') {
                ImagePositionSwap("image_0", element.id);
            } else {
                if (element.id == 'image_0'){
                    ImagePositionSwap("image_0", large_image[0].id);
                } else {
                    ImagePositionSwap(large_image[0].id, element.id);
                    ImagePositionSwap("image_0", element.id);
                }
            };

        };
    });
});

function ImagePositionSwap(BeSwapId, ToSwapId){
    const be_swap_img = document.getElementById(BeSwapId);
    const to_swap_img = document.getElementById(ToSwapId);
    const tmp_id = be_swap_img.id;
    const tmp_src = be_swap_img.src;
    be_swap_img.src = to_swap_img.src;
    to_swap_img.src = tmp_src;
    be_swap_img.id = ToSwapId;
    to_swap_img.id = tmp_id;
    };
