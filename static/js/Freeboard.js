function toggleDropdown() {
    var dropdownContent = document.getElementById("dropdown-content");
    if (dropdownContent.style.display === "none" || dropdownContent.style.display === "") {
        dropdownContent.style.display = "block";
    } else {
        dropdownContent.style.display = "none";
    }
}

function filterContent() {
    // 현재 선택된 카테고리와 정렬 옵션을 가져옵니다.
    var selectedCategories = document.querySelectorAll('input[name="category"]:checked');
    var sortOption = document.querySelector('input[name="sortOption"]:checked').value;

    console.log(selectedCategories);
    console.log("--------");
    console.log(sortOption);
    console.log("--------");
    // 필터링 로직 구현 구간
    // 예: AJAX를 사용하여 서버에 필터링 요청을 보내거나 페이지의 내용을 동적으로 변경합니다.
}