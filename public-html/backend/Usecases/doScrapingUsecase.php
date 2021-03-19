<?php

namespace backend\Usecases;

require_once __DIR__ . "/../../vendor/autoload.php";

use DOMWrap\Document;
use GuzzleHttp\Client;

class doScrapingUsecase
{
    private Client $_client;
    private Document $_document;

    public function __construct(Client $client, Document $document)
    {
        $this->_client = $client;
        $this->_document = $document;
    }

    /**
     * execute Scraping on the instructed url  
     *
     * @param string $url the target url to be scraped
     * @return string $node the html from the url
     */
    public static function doScraping(string $url)
    {
        $response = self::$_client->get($url);
        $html = (string)$response->getBody();
        $node = self::$_document->html($html);
        return $node;
    }
}
