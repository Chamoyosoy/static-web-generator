# Static Web Generator

This is a simple static web generator that takes content from the `content` directory, applies it to the `template.html` template, and generates a static website in the `public` directory.

## Configuration

The following configuration variables can be found in `src/config.py`:

*   `STATIC_DIR`: The directory containing static assets (CSS, JavaScript, images, etc.). Defaults to `./static/`.
*   `CONTENT_DIR`: The directory containing the content files to be used to generate the static pages. Defaults to `./content/`.
*   `TARGET_DIR`: The directory where the generated static website will be placed. Defaults to `./public/`.
*   `TEMPLATE`: The path to the HTML template file. Defaults to `./template.html`.

## Usage

1.  Place your content files.md in the `content` directory.
2.  Customize the `template.html` template to match your desired website structure.
3.  Place your static files (CSS, JavaScript, images, etc.) in the `static` directory.
4.  Run the `build.sh` script to generate the static website:

    ```bash
    ./build.sh
    ```

5.  The generated website will be located in the `public` directory.


## things to add
- [ ] configuration funtion
- [ ] automatic header with navigation bar
- [ ] automatic footer with contact info and page info
- [ ] RSS feed
