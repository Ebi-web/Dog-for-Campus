<?php

namespace backend\eachHps\generalEducation;

class generalEducation
{
    private $prefixInTargetUrl = "http://www2.he.tohoku.ac.jp/zengaku/";
    private $targetDirectoriesList = [
        "zengaku_info_g.html",
        "zengaku_annai.html",
        "zengaku_itiran.html",
        "zengaku_adp_g.html",
        "zengaku_others.html",
    ];
    public static function domOfgeneralEducation()
    {
        $prefixInTargetUrl = self::$prefixInTargetUrl;
        $targetDirectoriesList = self::$targetDirectoriesList;
    }
}
