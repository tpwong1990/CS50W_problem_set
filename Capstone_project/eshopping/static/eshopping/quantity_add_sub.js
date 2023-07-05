function quantity_add(target){
    const quantity_box = document.getElementsByClassName(target);
    let current_quantity = quantity_box[0].value;
    current_quantity = parseInt(current_quantity) + parseInt(1);
    //console.log(current_quantity);
    quantity_box[0].value = current_quantity;
};

function quantity_sub(target){
    const quantity_box = document.getElementsByClassName(target);
    let current_quantity = quantity_box[0].value;
    if (current_quantity >= 2) {
        current_quantity = parseInt(current_quantity) - parseInt(1);
    };
    //console.log(current_quantity);
    quantity_box[0].value = current_quantity;
};