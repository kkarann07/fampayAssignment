/* main.js */

// Pagination
//const paginationLinks = document.querySelectorAll('.pagination li a');
//paginationLinks.forEach(link => {
//    link.addEventListener('click', event => {
//        event.preventDefault();
//        const pageUrl = link.href;
//        fetch(pageUrl)
//            .then(response => response.json())
//            .then(data => {
//                const resultsHtml = data.results.map(video => {
//                    return `
//                        <div class="card mb-3">
//                            <div class="card-body">
//                                <h5 class="card-title">${video.title}</h5>
//                                <p class="card-text">${video.description}</p>
//                                <a href="${video.url}" class="btn btn-primary">Watch video</a>
//                                <small class="text-muted">${video.publish_datetime}</small>
//                            </div>
//                        </div>
//                    `;
//                }).join('');
//
//                document.querySelector('.content').innerHTML = resultsHtml;
//
//                // Update pagination links
//                document.querySelector('.pagination').innerHTML = '';
//                for (let i = 1; i <= data.num_pages; i++) {
//                    const activeClass = i === data.current_page_number ? 'active' : '';
//                    document.querySelector('.pagination').insertAdjacentHTML('beforeend', `
//                        <li class="page-item ${activeClass}">
//                            <a class="page-link" href="?page=${i}">${i}</a>
//                        </li>

