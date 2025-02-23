// Fetch all Token IDs from the page
const tokenIds = Array.from(document.querySelectorAll('span.text-gray-600')).map(span => {
    // Extract Token ID text and clean it
    const text = span.textContent.trim();
    const tokenId = text.replace('Token ID: ', '').trim();
    return tokenId;
});

// Create CSV content
const csvContent = "data:text/csv;charset=utf-8," + tokenIds.join("\n");

// Create a link to download the CSV file
const encodedUri = encodeURI(csvContent);
const link = document.createElement("a");
link.setAttribute("href", encodedUri);
link.setAttribute("download", "token_ids.csv");

// Append link to body and simulate click to download
document.body.appendChild(link);
link.click();

// Remove the link element after download
document.body.removeChild(link);
