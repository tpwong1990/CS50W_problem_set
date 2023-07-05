function page_navigator_search(current_page, search_text){
    const temp = document.getElementsByClassName("total_page_no");
    const total = temp[0].dataset.total_page_no;
    //console.log(`total: ${total}`);
    //console.log(`current: ${current_page}`);
    
    //Enable or diable previous button
    if (current_page == 1) {
        let previous_button = document.getElementById("previous_page");
        previous_button.setAttribute('class', "page-item disabled");
        previous_button.innerHTML = '<a class="page-link" href="#" aria-label="Previous" aria-disabled="true"><span aria-hidden="true">&laquo;</span></a>';
    } else {
        let previous_button = document.getElementById("previous_page");
        previous_button.setAttribute('class', "page-item");
        previous_button.innerHTML = `<a class="page-link" href="javascript:load_grid_items_search(${current_page - 1}, '${search_text}')" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a>`;
    };

    //Enable or diable Next button
    if (current_page == total) {
        let next_button = document.getElementById("next_page");
        next_button.setAttribute('class', "page-item disabled");
        next_button.innerHTML ='<a class="page-link" href="#" aria-label="Next" aria-disabled="true"><span aria-hidden="true">&raquo;</span></a>';
    } else {
        let next_button = document.getElementById("next_page");
        next_button.setAttribute('class', "page-item");
        next_button.innerHTML =`<a class="page-link" href="javascript:load_grid_items_search(${current_page + 1}, '${search_text}')" aria-label="Next"><span aria-hidden="true">&raquo;</span></a>`;
    };

    // Page button display
    if (total <= 7) {
        for (var i = 1; i <= total; i++) {
            let temp = `${i}th`;
            //console.log(temp);
            let li = document.getElementById(temp);
            li.removeAttribute("hidden");
            if ( i == current_page) {
                li.setAttribute('class', "page-item active");
                li.setAttribute('aria-current', "page");
                li.innerHTML = `<a class="page-link" href="#">${i}</a>`;
            } else {
                li.setAttribute('class', "page-item");
                li.removeAttribute("aria-current");
                li.innerHTML = `<a class="page-link" href="javascript:load_grid_items_search(${i}, '${search_text}')">${i}</a>`;
            };
        };
        // Remove exact button
        //console.log(`t:${total}`);
        let temp1 = parseInt(total) + parseInt(1);
        for (var j = temp1; j <= 7; j++) {
            let temp = `${j}th`;
            //console.log(temp);
            let li = document.getElementById(temp);
            li.setAttribute("hidden", true);
        };
    } else {
        if (current_page <= 3) {
            // Set first 5 button 
            for (var i = 1; i <= 5; i++) {                
                let temp = `${i}th`;
                let li = document.getElementById(temp);
                if ( i == current_page) {
                    li.setAttribute('class', "page-item active");
                    li.setAttribute('aria-current', "page");
                    li.innerHTML = `<a class="page-link" href="#">${i}</a>`;
                } else {
                    li.setAttribute('class', "page-item");
                    li.removeAttribute("aria-current");
                    li.innerHTML = `<a class="page-link" href="javascript:load_grid_items_searcg(${i}, '${search_text}')">${i}</a>`;
                };
            };
            // Set last - 1 button
            let temp = `6th`;
            let li = document.getElementById(temp);
            li.setAttribute('class', "page-item disabled");
            li.removeAttribute("aria-current");
            li.innerHTML = '<a class="page-link" href="#" aria-disabled="true">...</a>';

            // Set last button
            temp = `7th`;
            li = document.getElementById(temp);
            li.setAttribute('class', "page-item");
            li.removeAttribute("aria-current");
            li.innerHTML = `<a class="page-link" href="javascript:load_grid_items_search(${total}, '${search_text}')">${total}</a>`
        };

        if (current_page > 3 && current_page < total - 3) {
            // Set the first button
            let temp = `1th`;
            let li = document.getElementById(temp);
            li.setAttribute('class', "page-item");
            li.removeAttribute("aria-current");
            li.innerHTML = `<a class="page-link" href="javascript:load_grid_items_search(1, '${search_text}')">1</a>`;

            // Set the second button
            temp = `2th`;
            li = document.getElementById(temp);
            li.setAttribute('class', "page-item disabled");
            li.removeAttribute("aria-current");
            li.innerHTML = '<a class="page-link" href="#" aria-disabled="true">...</a>';

            // Set current -1, current, current + 1 button
            for (var i = 3; i <= 5; i++) {
                let temp = `${i}th`;
                let li = document.getElementById(temp);
                if ( i == 4) {
                    li.setAttribute('class', "page-item active");
                    li.setAttribute('aria-current', "page");
                    li.innerHTML = `<a class="page-link" href="#">${current_page}</a>`;
                } else {
                    li.setAttribute('class', "page-item");
                    li.removeAttribute("aria-current");
                    if (i == 3) {
                        li.innerHTML = `<a class="page-link" href="javascript:load_grid_items_search(${current_page-1}, '${search_text}')">${current_page-1}</a>`;
                    };
                    if (i == 5) {
                        li.innerHTML = `<a class="page-link" href="javascript:load_grid_items_search(${current_page+1}, '${search_text}')">${current_page+1}</a>`;    
                    }
                };
            };

            // Set last - 1 button
            temp = `6th`;
            li = document.getElementById(temp);
            li.setAttribute('class', "page-item disabled");
            li.removeAttribute("aria-current");
            li.innerHTML = '<a class="page-link" href="#" aria-disabled="true">...</a>';

            // Set last button
            temp = `7th`;
            li = document.getElementById(temp);
            li.setAttribute('class', "page-item");
            li.removeAttribute("aria-current");
            li.innerHTML = `<a class="page-link" href="javascript:load_grid_items_search(${total}, '${search_text}')">${total}</a>`
        };

        if (current_page >= total - 3){
            // Set the first button
            let temp = `1th`;
            let li = document.getElementById(temp);
            li.setAttribute('class', "page-item");
            li.removeAttribute("aria-current");
            li.innerHTML = `<a class="page-link" href="javascript:load_grid_items_search(1, '${search_text}')">1</a>`;

            // Set the second button
            temp = `2th`;
            li = document.getElementById(temp);
            li.setAttribute('class', "page-item disabled");
            li.removeAttribute("aria-current");
            li.innerHTML = '<a class="page-link" href="#" aria-disabled="true">...</a>';

            // Set the last 5 button
            for (var i = 3; i <= 7; i++) {
                let temp = `${i}th`;
                let li = document.getElementById(temp);
                if (current_page == total-(7-i)) {
                    li.setAttribute('class', "page-item active");
                    li.setAttribute('aria-current', "page");
                    li.innerHTML = `<a class="page-link" href="#">${current_page}</a>`;
                } else {
                    li.setAttribute('class', "page-item");
                    li.removeAttribute("aria-current");
                    li.innerHTML = `<a class="page-link" href="javascript:load_grid_items_search(${total-(7-i)}, '${search_text}')">${total-(7-i)}</a>`;
                };
            };

        };
    };
};