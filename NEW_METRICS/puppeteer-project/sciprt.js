const puppeteer = require('puppeteer'); // v22.0.0 or later

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const timeout = 30000;
    page.setDefaultTimeout(timeout);

    try {
        // Navegar a la página específica antes de ejecutar el script
        await page.goto('URL_DE_LA_PAGINA_A_CARGAR', { waitUntil: 'domcontentloaded' });

        // Ajustar el tamaño de la ventana si es necesario
        await page.setViewport({
            width: 680,
            height: 957
        });

        // Realizar el primer click
        await puppeteer.Locator.race([
            page.locator('div.gui_menu-bar-position_3U1T0 div:nth-of-type(3) > img:nth-of-type(1)'),
            page.locator('::-p-xpath(//*[@id=\\"app\\"]/div/div[2]/div[1]/div[1]/div[3]/img[1])'),
            page.locator(':scope >>> div.gui_menu-bar-position_3U1T0 div:nth-of-type(3) > img:nth-of-type(1)')
        ])
        .setTimeout(timeout)
        .click({
            offset: {
                x: 17.515625,
                y: 16,
            },
        });

        // Realizar el segundo click
        await puppeteer.Locator.race([
            page.locator('li:nth-of-type(4) > span'),
            page.locator('::-p-xpath(//*[@id=\\"app\\"]/div/div[2]/div[1]/div[1]/div[3]/div/ul/li[4]/span)'),
            page.locator(':scope >>> li:nth-of-type(4) > span'),
            page.locator('::-p-text(Save to your)')
        ])
        .setTimeout(timeout)
        .click({
            offset: {
                x: 70.515625,
                y: 5,
            },
        });

        // Cerrar el navegador al finalizar
        await browser.close();
    } catch (err) {
        console.error(err);
        process.exit(1);
    }
})();

