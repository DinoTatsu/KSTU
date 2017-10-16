using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace TMproj.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            int q = 7;
            int w = 5;
            int sum = q + w;
            ViewBag.q = q;
            ViewBag.w = 5;
            ViewBag.sum = sum;
            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }
    }
}