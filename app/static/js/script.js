document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById("Product_label");

    form.onsubmit = function () {
        return validateForm();
    };

    function validateForm() {
        var input = document.querySelector("input[name='file']");
        var files = input.files;
        var requiredExtensions = [".shp", ".dbf", ".shx"];
        var requiredFileCount = requiredExtensions.length;
        var foundFileCount = 0;

        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            var fileName = file.name;
            var fileSize = file.size;
            var fileExtension = fileName.substr(fileName.lastIndexOf("."));

            if (requiredExtensions.includes(fileExtension)) {
                foundFileCount++;
                if (fileSize > 5 * 1024 * 1024) {
                    alert("The maximum supported file size is 5 MB. " + fileName + " exceeds the size limit.");
                    return false;
                }
            }
        }

        if (foundFileCount < requiredFileCount) {
            alert("The *.shp, *.dbf, and *shx files are required for uploaded shapefiles");
            return false;
        }

        return true;
    }
});