using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Data.Entity;

namespace TMproj.Models
{
    public class BlogContext : DbContext
    {
         public DbSet<Note> Notes {get; set; }
    }
}