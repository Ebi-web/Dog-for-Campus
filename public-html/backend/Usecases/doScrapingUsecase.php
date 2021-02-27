<?php

namespace backend\Usecases\doScrapingUsecase;

class doScrapingUsecase
{
    public static function doScraping(string $url)
    {
        $html = file_get_contents($url);
        $dom = null;
        $dom = phpQuery::newDocument($html);
        return $dom;
    }
}
