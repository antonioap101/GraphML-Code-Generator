class FileDownloader {
    /**
     * Triggers a file download with the given content, filename, and MIME type.
     * @param content The content to be downloaded.
     * @param filename The name of the file to be downloaded.
     * @param mimeType The MIME type of the file.
     */
    static download(content: BlobPart, filename: string, mimeType: string): void {
        // Create a Blob from the content
        const blob = new Blob([content], {type: mimeType});

        // Create a URL for the Blob
        const url = URL.createObjectURL(blob);

        // Create a temporary anchor element to trigger the download
        const link = document.createElement('a');
        link.href = url;
        link.download = filename;

        // Append the anchor to the body (required for Firefox)
        document.body.appendChild(link);

        // Trigger the download
        link.click();

        // Clean up by removing the anchor and revoking the Blob URL
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }
}


// Example usage:
/**
 * const downloadExample = () => {
 *     const graphmlOutput = '<graphml></graphml>'; // Example content
 *     FileDownloader.download(graphmlOutput, 'output.graphml', 'application/xml');
 * };
 */

export default FileDownloader;