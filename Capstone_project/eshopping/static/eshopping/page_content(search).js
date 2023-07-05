function load_grid_items_search(page_no, search_text) {
    const temp = document.getElementsByClassName("no_of_box");
    const box_no = temp[0].dataset.no_of_box;
    //console.log(box_no);

    // Get items details
    fetch(`/search_page_content/${page_no}/${search_text}`)
    .then(response => response.json())
    .then(result=> {
        //console.log(result);
        var items = JSON.parse(result);
        items.forEach(function (element, i) {
            //console.log(i+1);
            //console.log(element.fields.image);
            item_box_content((i+1).toString() ,element);
        });
        if (items.length < box_no){
            //console.log(count_left);
            for (var i = items.length+1; i <= box_no; i++) {
                //console.log(i);
                item_box_content_empty(i.toString());
            };
        };
        // Get page navigator
        page_navigator_search(page_no, search_text);
    });
};