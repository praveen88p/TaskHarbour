document.addEventListener('DOMContentLoaded', () => {
    const ImgGenLink = document.getElementById('image-link');
    const searchBarMain = document.getElementById('search-bar-main');

    ImgGenLink.addEventListener('click', (event) => {
        event.preventDefault(); // prevent the default link behavior
        if (searchBarMain) {
            searchBarMain.innerHTML = `
            <form id="search-form" method="post" enctype="multipart/form-data">
           
            <input id="inputText" type="text" name="user_input" placeholder="Enter a search term...">
            <button id="image-button" type="submit" name="action" value="image">Generate Image</button>
        </form>
            `;
        }
    });
});
