document.addEventListener('DOMContentLoaded', function () {
    var fileInput = document.querySelector("input[type=file]");
    fileInput.onchange = function () {
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
                if (fileSize > 100 * 1024 * 1024) {
                    alert("The maximum supported file sizes are 5 MB. " + fileName + " exceed the size limit.");
                    fileInput.value = "";
                    return;
                }
            }
        }

        if (foundFileCount < requiredFileCount) {
            alert("The *.shp, *.dbf, and *shx files are required for uploaded shapefiles");
            fileInput.value = "";
            return;
        }

        document.getElementById("Product_label").submit();
    };

    function validateForm() {
        var fileInput = document.querySelector("input[type=file]");
        var files = fileInput.files;
        var requiredExtensions = [".shp", ".dbf", ".shx"];
        var requiredFileCount = requiredExtensions.length;
        var foundFileCount = 0;

        for (var i = 0; i < files.length; i++) {
            var file = files[i];
            var fileName = file.name;
            var fileExtension = fileName.substr(fileName.lastIndexOf("."));

            if (requiredExtensions.includes(fileExtension)) {
                foundFileCount++;
            }
        }

        if (foundFileCount < requiredFileCount) {
            alert("The *.shp, *.dbf, and *shx files are required for uploaded shapefiles");
            return false;
        }

        return true;
    }
});