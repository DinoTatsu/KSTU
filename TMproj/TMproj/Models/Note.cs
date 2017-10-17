using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace TMproj.Models
{
    public class Note
    {
        public int noteID { get; set; }
        public DateTime created { get; set; }
        public string title { get; set; }
        public string article { get; set; }
    }
}