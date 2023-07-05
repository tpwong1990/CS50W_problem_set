function item_box_content(box_name, item){

    // Get item box div
    //console.log(`box_name: ${box_name}`);
    let div_box = document.getElementsByName(box_name);
    //console.log(div_box);

    // Set item box id and onclick function
    div_box[0].setAttribute('class', "item_box");
    div_box[0].setAttribute('id', item.pk);
    div_box[0].setAttribute('onclick', `location.href='/item_detail/${item.pk}'`);
    div_box[0].innerHTML = '';

    // Set image div
    const image_div = document.createElement("div")
    image_div.setAttribute('class', "image_block");
    image_div.style.width = "auto";
    const image_tag = document.createElement("img")
    if (item.fields.cover_image == ''){
        const no_image_link ="https://media.istockphoto.com/id/1357365823/vector/default-image-icon-vector-missing-picture-page-for-website-design-or-mobile-app-no-photo.jpg?s=1024x1024&w=is&k=20&c=FGIHlElBCl9f52B_974wFjOxOj_yGSZIYJcbYtRZGP8=";
        image_tag.setAttribute('src', no_image_link);
    } else {
        image_tag.setAttribute('src', `/static/${item.fields.cover_image}`);
    };
    image_tag.style.width = "100%";
    image_tag.style.maxWidth = "250px";

    // Append the image to item box div
    const img_block = div_box[0].getElementsByClassName("image_block");
    div_box[0].appendChild(image_div);
    img_block[0].appendChild(image_tag);

    // Create and append span tag for item name
    const item_name = document.createElement("span");
    item_name.innerHTML = `${item.fields.name}`;
    div_box[0].appendChild(item_name);
    div_box[0].appendChild(document.createElement("br"));

    // Create and append span tag for item price
    const item_price = document.createElement("span");
    if (item.fields.updated_price > 0) {
        item_price.innerHTML = `$ <del>${item.fields.price}</del> ${item.fields.updated_price}`;
    } else {
        item_price.innerHTML = `$ ${item.fields.price}`;
    };
    div_box[0].appendChild(item_price);

    // Check stock
    if (item.fields.stock == 0) {
        item_name.innerHTML = `${item.fields.name} <span class="badge badge-secondary">Sold Out</span>`;
    }
    };

function item_box_content_empty(box_name){
    let div_box = document.getElementsByName(box_name);
    //console.log(div_box);
    div_box[0].setAttribute('class', "item_box_empty");
    div_box[0].removeAttribute('id');
    div_box[0].removeAttribute("onclick");
    div_box[0].innerHTML ='';
};

