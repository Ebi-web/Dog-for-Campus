<?php

namespace backend\eachHps;

use backend\Usecases\doScrapingUsecase;

class unvHp
{
    private const url = "https://www.tohoku.ac.jp/japanese/rss/cate_tar_student/index.xml";
    public static function domOfUnvHp()
    {
        $url = self::url;
        $rawDom = doScrapingUsecase::doScraping($url);
        $dom = $rawDom->not("id");
        return $dom;
    }
}
