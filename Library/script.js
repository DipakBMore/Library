document.getElementById("addBtn").addEventListener("click", function () {

    const input = document.getElementById("libraryInput");
    const libraryName = input.value.trim();

    if (libraryName === "") {
        alert("Please enter a library name.");
        return;
    }

    const libraryList = document.getElementById("libraryList");

    const libraryItem = document.createElement("div");
    libraryItem.className = "library-item";

    libraryItem.innerHTML = `
        <span>${libraryName}</span>
        <button class="view-btn">View</button>
    `;

    libraryItem.querySelector(".view-btn").addEventListener("click", function () {
        alert("Viewing Library: " + libraryName);
    });

    libraryList.appendChild(libraryItem);

    input.value = "";

    libraryItem.innerHTML = `
    <span>${libraryName}</span>
    <button class="view-btn" onclick="viewLibrary('${libraryName}')">
        View
    </button>
`;
});

function viewLibrary(libraryName) {
    alert("Viewing Library: " + libraryName);
}