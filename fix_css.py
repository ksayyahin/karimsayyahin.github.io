import codecs

with open("css/styles.css", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()
clean_lines = lines[:818]

css_to_append = """
/* Engineering Data Table */
.engineering-table-container {
    overflow-x: auto;
    margin-bottom: var(--space-md);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    background: var(--card-bg);
}

.engineering-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.95rem;
    text-align: left;
}

.engineering-table th,
.engineering-table td {
    padding: 12px 16px;
    border-bottom: 1px solid var(--border-color);
}

.engineering-table th {
    font-weight: 600;
    color: var(--text-secondary);
    background-color: rgba(255, 255, 255, 0.02);
}

@media (prefers-color-scheme: light) {
    .engineering-table th {
        background-color: rgba(0, 0, 0, 0.02);
    }
}

.engineering-table tr:last-child td {
    border-bottom: none;
}

/* Specific Media Layouts */
.media-container {
    width: 100%;
    margin-bottom: var(--space-xs);
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border-color);
    background: var(--card-hover);
    display: flex;
    align-items: center;
    justify-content: center;
}

.media-container img,
.media-container video {
    width: 100%;
    height: auto;
    max-height: 500px;
    object-fit: contain;
    display: block;
}

.gallery-item .media-container {
    aspect-ratio: 4/3;
    max-height: none;
}

.gallery-item .media-container img,
.gallery-item .media-container video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    max-height: none;
}

.media-wide {
    margin: var(--space-lg) 0;
}
.media-wide img,
.media-wide video {
    max-height: 60vh;
}
"""

with open("css/styles.css", "w", encoding="utf-8") as f:
    f.writelines(clean_lines)
    f.write(css_to_append)
