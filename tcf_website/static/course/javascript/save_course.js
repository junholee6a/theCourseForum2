
function saveCourse() {
    $.ajax({
        type: "GET",
        url: `/save_course/${course_id}/${instructor_id}`
    });

    document.getElementById("saveCourseBtn").style = "display: none!important;";
    document.getElementById("unsaveCourseBtn").style = "display: auto;";
}

function unsaveCourse() {
    $.ajax({
        type: "GET",
        url: `/unsave_course/${course_id}/${instructor_id}`
    });

    document.getElementById("saveCourseBtn").style = "display: auto;";
    document.getElementById("unsaveCourseBtn").style = "display: none!important;";
}

document.getElementById("saveCourseBtn").addEventListener("click", saveCourse, false);
document.getElementById("unsaveCourseBtn").addEventListener("click", unsaveCourse, false);
