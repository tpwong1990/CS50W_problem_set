function load_grid_items(page_no, category_id){
    const temp = document.getElementsByClassName("no_of_box");
    const box_no = temp[0].dataset.no_of_box;

    // Get items details
    fetch(`/page_content/${page_no}/${category_id}`)
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
                }
        };
        // Get page navigator
        page_navigator(page_no, category_id);
    });
};

