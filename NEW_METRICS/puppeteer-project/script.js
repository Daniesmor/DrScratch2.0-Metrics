const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({ headless: false }); // Puedes usar headless: false para ver la navegación
    const page = await browser.newPage();
    const timeout = 60000; // Aumentar el timeout a 60 segundos
    page.setDefaultTimeout(timeout);

    try {
        // Navegar a la página específica antes de ejecutar el script
        await page.goto('https://scratch.mit.edu/projects/1032287582/editor/', { waitUntil: 'domcontentloaded' });

        // Ajustar el tamaño de la ventana si es necesario
        await page.setViewport({
            width: 680,
            height: 957
        });

        // Esperar y realizar el primer click
        await page.waitForSelector('div.gui_menu-bar-position_3U1T0 div:nth-of-type(3) > img:nth-of-type(1)', { timeout });
        await page.click('div.gui_menu-bar-position_3U1T0 div:nth-of-type(3) > img:nth-of-type(1)', {
            clickCount: 1,
            delay: 100
        });

      
        // Cerrar el navegador al finalizar
        await browser.close();
    } catch (err) {
        console.error(err);
        await browser.close(); // Asegurarse de cerrar el navegador en caso de error
        process.exit(1);
    }
})();
