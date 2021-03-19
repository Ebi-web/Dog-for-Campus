<?php

namespace backend\eachHps;

use backend\Usecases\doScrapingUsecase;
use DOMWrap\Document;
use GuzzleHttp\Client;

class unvHp
{
    private const url = "https://www.tohoku.ac.jp/japanese/rss/cate_tar_student/index.xml";
    private Client $_client;
    private Document $_document;


    public static function domOfUnvHp()
    {
        $url = self::url;
        $rawDom = doScrapingUsecase::doScraping($url);
        $dom = $rawDom->not("id");
        return $dom;
    }
}
